// One-off icon generator: renders public/icon.svg to the PNG sizes listed in
// the PWA manifest (astro.config.mjs). Run with `node src/pwa/make-icons.mjs`.
import sharp from 'sharp';
import { mkdir, readFile } from 'node:fs/promises';
import { fileURLToPath } from 'node:url';

const root = new URL('../../', import.meta.url);
const svg = await readFile(new URL('public/icon.svg', root));
const outDir = new URL('public/icons/', root);
await mkdir(outDir, { recursive: true });

// Maskable icons keep the glyph inside the 80% safe zone by padding the artwork.
const maskableSvg = Buffer.from(
	`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" width="512" height="512">
	  <rect width="512" height="512" fill="#7c3aed"/>
	  <g transform="translate(76 76) scale(0.703125)">
	    <path d="M136 152h240v64h-88v176h-64V216h-88z" fill="#fff"/>
	  </g>
	</svg>`,
);

for (const size of [192, 512]) {
	await sharp(svg).resize(size, size).png().toFile(fileURLToPath(new URL(`icon-${size}.png`, outDir)));
	await sharp(maskableSvg).resize(size, size).png().toFile(fileURLToPath(new URL(`icon-maskable-${size}.png`, outDir)));
	console.log(`icons/icon-${size}.png, icons/icon-maskable-${size}.png`);
}
