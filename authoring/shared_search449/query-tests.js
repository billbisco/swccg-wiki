'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const root = __dirname;
const engine = require('./product/query.js');
const data = JSON.parse(fs.readFileSync(path.join(root,'product/data.json'),'utf8'));
const cases = JSON.parse(fs.readFileSync(path.join(root,'query-cases.json'),'utf8'));
const original = JSON.stringify(data);
for (const test of cases) {
    if (test.error) assert.throws(()=>engine.search(data,test.query), e=>e.message.includes(test.error),test.name);
    else {
        const result=engine.search(data,test.query);
        assert.deepEqual(result.ids.slice().sort(),test.ids.slice().sort(),test.name);
        if(test.counts) assert.deepEqual(Object.fromEntries(result.records.map(r=>[r.id,r.matchedCount])),test.counts,test.name);
    }
}
// Unknowns are test-only controls, never fabricated production records.
const unknown=JSON.parse(JSON.stringify(data));unknown.cards=[Object.assign({},data.cards[0],{uniqueness:null,printedSymbol:null,referencedSymbols:[]})];
assert.equal(engine.search(unknown,{uniqueness:'unknown'}).records.length,1);
assert.equal(engine.search(unknown,{uniqueness:'unrestricted'}).records.length,0);
assert.equal(engine.search(unknown,{symbol:'None (Premiere)'}).records.length,0);
assert.equal(JSON.stringify(data),original,'Queries must not mutate the source or deck entries');
assert.deepEqual(data.decks.map(d=>d.mainCount),[60,60,60,60]);
assert.deepEqual(data.decks.map(d=>d.outsideCount),[0,5,23,29]);
console.log(cases.length+' independent public query cases and unknown/nonmutation/count controls PASS');
