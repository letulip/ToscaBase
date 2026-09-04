// Make the custom UI strings in src/content/i18n/*.json known to `Astro.locals.t()`.
declare namespace StarlightApp {
	type UIStrings = typeof import('./content/i18n/en.json');
	interface I18n extends UIStrings {}
}
