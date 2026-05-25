const fs = require('fs');
const path = require('path');

// Simple YAML frontmatter parser
function parseFrontmatter(content) {
  const match = content.match(/^---\r?\n([\s\S]*?)\r?\n---/);
  if (!match) return {};
  const yaml = match[1];
  const data = {};
  yaml.split('\n').forEach(line => {
    const [key, ...valueParts] = line.split(':');
    if (key && valueParts.length > 0) {
      data[key.trim()] = valueParts.join(':').trim();
    }
  });
  return data;
}

const analysisDir = path.join(__dirname, '../docs/analysis');
const manifestPath = path.join(__dirname, '../public/manifest.json');

if (!fs.existsSync(analysisDir)) {
  console.log('No analysis files found in docs/analysis. Creating directory...');
  fs.mkdirSync(analysisDir, { recursive: true });
  fs.writeFileSync(manifestPath, JSON.stringify([], null, 2));
  process.exit(0);
}

const files = fs.readdirSync(analysisDir).filter(f => f.endsWith('.md'));
const manifest = files.map(file => {
  const content = fs.readFileSync(path.join(analysisDir, file), 'utf-8');
  return {
    id: file.replace('.md', ''),
    ...parseFrontmatter(content)
  };
});

fs.writeFileSync(manifestPath, JSON.stringify(manifest, null, 2));
console.log(`Generated manifest.json with ${manifest.length} entries.`);
