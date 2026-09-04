import { defineCollection, z } from 'astro:content';
import { docsLoader, i18nLoader } from '@astrojs/starlight/loaders';
import { docsSchema, i18nSchema } from '@astrojs/starlight/schema';

/** A video (or other) source a page was reworked from. */
const sourceSchema = z.object({
	id: z.string(),
	title: z.string(),
	url: z.string().url(),
	/** Optional timestamp inside the source, e.g. "12:34". */
	at: z.string().optional(),
});

export const collections = {
	docs: defineCollection({
		loader: docsLoader(),
		schema: docsSchema({
			extend: z.object({
				sources: z.array(sourceSchema).optional(),
				/** Mastery level: 1 foundations, 2 building tests, 3 specialised, 4 enterprise. */
				level: z.number().int().min(1).max(4).optional(),
			}),
		}),
	}),
	i18n: defineCollection({
		loader: i18nLoader(),
		schema: i18nSchema({
			extend: z.object({
				'toscabase.sources': z.string().optional(),
				'toscabase.level': z.string().optional(),
			}),
		}),
	}),
};
