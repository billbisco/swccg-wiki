(function (root, factory) {
    if (typeof module === 'object' && module.exports) module.exports = factory();
    else root.SharedSearchQuery = factory();
}(typeof globalThis !== 'undefined' ? globalThis : this, function () {
    'use strict';
    const uniqueness = ['any', 'unique', 'unrestricted', 'restricted-2', 'restricted-3', 'restricted-6', 'diamond-1', 'diamond-2', 'diamond-3', 'unknown'];
    function normalize(value) {
        return String(value || '').normalize('NFKC').toLowerCase().replace(/[’']/g, '').replace(/[^a-z0-9]+/g, ' ').trim();
    }
    function symbolId(data, value) {
        const term = normalize(value);
        if (!term) return '';
        const symbol = data.symbols.find(s => [s.id, s.label].concat(s.aliases).some(v => normalize(v) === term));
        if (!symbol) throw new Error('Unknown set symbol. Choose a name from the suggestions.');
        return symbol.id;
    }
    function canonicalQuery(data, input) {
        input = input || {};
        const q = {
            mode: input.mode || 'cards', text: String(input.text || '').trim(),
            symbol: symbolId(data, input.symbol || ''), role: input.role || 'printed',
            uniqueness: input.uniqueness || 'any', contains: input.contains || '',
            identity: input.identity || 'family', zone: input.zone || 'main'
        };
        if (!['cards', 'decks'].includes(q.mode)) throw new Error('Choose Cards or Published decklists.');
        if (!['printed', 'referenced'].includes(q.role)) throw new Error('Choose printed symbol or game-text reference.');
        if (!uniqueness.includes(q.uniqueness)) throw new Error('Unknown uniqueness category.');
        if (!['family', 'recorded'].includes(q.identity)) throw new Error('Unknown card-identity mode.');
        if (!['main', 'all'].includes(q.zone)) throw new Error('Unknown deck section.');
        if (q.text.length > 200) throw new Error('Search text is limited to 200 characters.');
        if (q.contains && !data.cards.some(c => c.id === q.contains)) throw new Error('Choose a card from this pilot snapshot.');
        return q;
    }
    function textMatches(text, query) {
        const terms = normalize(query).split(' ').filter(Boolean);
        return terms.every(term => normalize(text).includes(term));
    }
    function cardMatches(data, card, q) {
        if (q.uniqueness !== 'any' && (card.uniqueness || 'unknown') !== q.uniqueness) return false;
        if (q.symbol && !(q.role === 'printed' ? card.printedSymbol === q.symbol : card.referencedSymbols.includes(q.symbol))) return false;
        const relatedSymbols = data.symbols.filter(s => [card.printedSymbol].concat(card.referencedSymbols).includes(s.id));
        const searchable = [card.title, card.product, card.text, card.id, card.familyId, card.recordedId || '']
            .concat(relatedSymbols.flatMap(s => [s.label].concat(s.aliases))).join(' ');
        return textMatches(searchable, q.text);
    }
    function deckCount(deck, card, q) {
        if (q.identity === 'recorded' && !card.recordedId) throw new Error('This printing has no verified exact import ID. Use card-family matching.');
        return deck.entries.filter(e => (q.zone === 'all' || e.zone === 'main') &&
            (q.identity === 'family' ? e.familyId === card.familyId : e.recordedId === card.recordedId))
            .reduce((sum, e) => sum + e.count, 0);
    }
    function search(data, input) {
        const q = canonicalQuery(data, input);
        let records;
        if (q.mode === 'cards') records = data.cards.filter(c => cardMatches(data, c, q));
        else {
            // Card-only controls have no hidden meaning in deck discovery.
            if (q.symbol || q.uniqueness !== 'any') throw new Error('Symbol and uniqueness filters apply to Cards. Clear them for deck discovery.');
            const card = q.contains ? data.cards.find(c => c.id === q.contains) : null;
            records = data.decks.filter(d => textMatches([d.title, d.player, d.event, d.format].join(' '), q.text))
                .map(d => Object.assign({}, d, {matchedCount: card ? deckCount(d, card, q) : null}))
                .filter(d => !card || d.matchedCount > 0);
        }
        records.sort((a, b) => a.title.localeCompare(b.title, 'en') || a.id.localeCompare(b.id, 'en'));
        return {schemaVersion: 1, snapshotId: data.snapshotId, query: q, kind: q.mode, ids: records.map(r => r.id), records: records};
    }
    return {normalize: normalize, symbolId: symbolId, canonicalQuery: canonicalQuery, search: search, deckCount: deckCount};
}));
