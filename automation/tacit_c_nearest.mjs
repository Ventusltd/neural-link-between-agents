import {readFileSync} from 'node:fs';
import {parse,version} from 'acorn';
if(version!=='8.15.0')throw Error('parser version');
const tree=parse(readFileSync(process.argv[2],'utf8'),{ecmaVersion:'latest',sourceType:'module',locations:true});
const imports=tree.body.filter(n=>n.type==='ImportDeclaration');
if(imports.length!==1||imports[0].specifiers.length!==1||imports[0].specifiers[0].imported.name!=='distanceKm'||imports[0].specifiers[0].local.name!=='distanceKm')throw Error('import contract');
let nearest, calls=[];
function visit(n,anc=[]){
 if(!n||typeof n!=='object')return;
 if(n.type==='Property'&&n.key?.name==='nearest'&&n.value?.type==='ArrowFunctionExpression'){
  if(nearest||!anc.some(a=>a.type==='FunctionDeclaration'&&a.id?.name==='index'))throw Error('nearest scope');
  nearest=n;
 }
 if(n.type==='ImportExpression'||(n.type==='CallExpression'&&['eval','require','Function'].includes(n.callee?.name)))throw Error('dynamic dependency');
 if(n.type==='CallExpression'&&n.callee.type==='Identifier')calls.push({name:n.callee.name,line:n.loc.start.line});
 for(const [k,v] of Object.entries(n))if(k!=='loc'){if(Array.isArray(v))v.forEach(x=>visit(x,[...anc,n]));else visit(v,[...anc,n]);}
}
visit(tree);
if(!nearest||!calls.some(c=>c.name==='normalise'&&c.line===54)||!calls.some(c=>c.name==='distanceKm'&&c.line===81))throw Error('missing static call');
console.log(JSON.stringify({static_import:{from:'engine/v9-nearest-search.js',to:'engine/v9-geodesy.js',symbol:imports[0].specifiers[0].imported.name},nearest:{first:nearest.loc.start.line,last:nearest.loc.end.line,col0:nearest.loc.start.column,col1:nearest.loc.end.column,kind:'nested_property_not_export'},calls}));
if(imports[0].source.value!=='./v9-geodesy.js')throw Error('wrong import path');
