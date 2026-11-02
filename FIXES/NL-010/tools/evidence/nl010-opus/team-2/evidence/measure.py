import json, sys, collections
d = json.load(open(sys.argv[1]))
B = d['bodies']
placed = [b for b in B if b.get('on_wafer')]
print('bodies', len(B), 'placed', len(placed))
print('placed with line_text field', sum('line_text' in b and b['line_text'] is not None for b in placed))
print('unplaced with line_text', [(b['repo'], b['id'], 'line_text' in b) for b in B if not b.get('on_wafer')])
empty = [b for b in placed if b['line_text'] == '']
nonempty = [b for b in placed if b['line_text'] != '']
print('empty line_text', len(empty), 'nonempty', len(nonempty))
eq = [b for b in nonempty if b['quote'] == b['line_text']]
print('nonempty quote==line_text', len(eq), 'differ', len(nonempty) - len(eq))
print('all placed quote==line_text', sum(b['quote'] == b['line_text'] for b in placed), 'differ (incl empty)', sum(b['quote'] != b['line_text'] for b in placed))
print('quote_check counts (placed):', dict(collections.Counter(b['quote_check'] for b in placed)))
print('quote_check by empty:', dict(collections.Counter(b['quote_check'] for b in empty)))
ws = [b for b in nonempty if b['quote'] != b['line_text'] and b['quote'].strip() == b['line_text'].strip()]
print('differ only by surrounding whitespace (strip)', len(ws))
ws2 = [b for b in nonempty if b['quote'] != b['line_text'] and b['quote'] == b['line_text'].lstrip()]
print('quote == line_text.lstrip()', len(ws2))
print('quote_key present', sum('quote_key' in b for b in placed))
for b in empty: print(' EMPTY', b['repo'], b['path'], b['line'], b['key'], b['quote_check'])
