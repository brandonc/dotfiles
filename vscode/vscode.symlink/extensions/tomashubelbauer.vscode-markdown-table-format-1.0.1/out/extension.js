'use strict';
Object.defineProperty(exports, "__esModule", { value: true });
const vscode_1 = require("vscode");
const markdown_dom_1 = require("markdown-dom");
function activate(context) {
    const tableFormatter = new TableFormatter();
    vscode_1.languages.registerDocumentFormattingEditProvider('markdown', tableFormatter);
}
exports.activate = activate;
class TableFormatter {
    provideDocumentFormattingEdits(document, _options, _token) {
        const tables = [];
        let table = false;
        for (let index = 0; index < document.lineCount; index++) {
            const line = document.lineAt(index);
            if (line.text.startsWith('|')) {
                if (!table) {
                    tables.push({ lines: [line.text], start: line.range.start });
                    table = true;
                }
                else {
                    tables[tables.length - 1].lines.push(line.text);
                }
            }
            else {
                if (table) {
                    const currentTable = tables[tables.length - 1];
                    currentTable.end = line.range.start;
                    table = false;
                }
            }
        }
        // Include last row in the document not followed by a newline to the last table
        if (table) {
            const currentTable = tables[tables.length - 1];
            currentTable.end = document.lineAt(document.lineCount - 1).range.end;
        }
        const edits = [];
        for (const table of tables) {
            // TODO: Preserve original line endings and parse those to be able to emit the correct ones again
            const dom = markdown_dom_1.default.parse(table.lines.join('\n'));
            if (dom.blocks.length !== 1) {
                // TODO: Report error to telemetry.
                continue;
            }
            const block = dom.blocks[0];
            if (block.type !== 'table') {
                // TODO: Report error to telemetry.
                continue;
            }
            const { header, body } = block;
            // Pop the dash row if any.
            if (body[0].find(cell => cell.replace(/[- ]/g, '') === '')) {
                body.shift();
            }
            const lengths = [];
            // TODO: Fix the extra phantom cell in MarkDownDOM.
            header.pop();
            for (let index = 0; index < header.length; index++) {
                lengths[index] = Math.max(lengths[index] || 0, header[index].trim().length);
            }
            for (const row of body) {
                // TODO: Fix the extra phantom cell in MarkDownDOM.
                row.pop();
                for (let index = 0; index < row.length; index++) {
                    lengths[index] = Math.max(lengths[index] || 0, row[index].trim().length);
                }
            }
            let markdown = '';
            // Insert the header.
            markdown += '|';
            for (let index = 0; index < lengths.length; index++) {
                markdown += ` ${(header[index] || '').trim().padEnd(lengths[index])} |`;
            }
            // TODO: Read correct line breaks from MarkDownDOM.
            markdown += '\n';
            // Insert the dashes.
            markdown += '|';
            for (let index = 0; index < lengths.length; index++) {
                markdown += '-'.repeat(lengths[index] + 2).padEnd(lengths[index]) + '|';
            }
            // TODO: Read correct line breaks from MarkDownDOM.
            markdown += '\n';
            // Insert the rows.
            for (const row of body) {
                markdown += '|';
                for (let index = 0; index < lengths.length; index++) {
                    markdown += ` ${(row[index] || '').trim().padEnd(lengths[index])} |`;
                }
                // TODO: Read correct line breaks from MarkDownDOM.
                markdown += '\n';
            }
            edits.push(vscode_1.TextEdit.replace(new vscode_1.Range(table.start, table.end), markdown));
        }
        return edits;
    }
}
//# sourceMappingURL=extension.js.map