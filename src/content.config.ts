import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    publishedAt: z.coerce.date(),
    updatedAt: z.coerce.date().optional(),
    author: z.string().default('Silence Team'),
    tags: z.array(z.string()).default([]),
    coverImage: z.string().optional(),
    draft: z.boolean().default(false),
  }),
});

const changelog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/changelog' }),
  schema: z.object({
    version: z.string(),
    releasedAt: z.coerce.date(),
    title: z.string(),
    summary: z.string(),
    highlights: z.array(z.string()).default([]),
  }),
});

const docs = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/docs' }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    module: z.string().optional(),
    order: z.number().default(99),
    section: z.string().optional(),
    draft: z.boolean().default(false),
  }),
});

const modules = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/modules' }),
  schema: z.object({
    title: z.string(),
    tagline: z.string(),
    description: z.string(),
    icon: z.string(),
    slug: z.string(),
    order: z.number().default(99),
    features: z.array(z.object({
      title: z.string(),
      description: z.string(),
      icon: z.string(),
    })).default([]),
    replaces: z.array(z.string()).default([]),
  }),
});

const caseStudies = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/case-studies' }),
  schema: z.object({
    title: z.string(),
    company: z.string(),
    industry: z.string(),
    description: z.string(),
    results: z.array(z.object({
      metric: z.string(),
      value: z.string(),
    })).default([]),
    logo: z.string().optional(),
    publishedAt: z.coerce.date(),
    featured: z.boolean().default(false),
  }),
});

const comparisons = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/comparisons' }),
  schema: z.object({
    title: z.string(),
    competitor: z.string(),
    competitorSlug: z.string(),
    description: z.string(),
    publishedAt: z.coerce.date(),
    verdict: z.string(),
    features: z.array(z.object({
      name: z.string(),
      silence: z.boolean(),
      competitor: z.boolean(),
      note: z.string().optional(),
    })).default([]),
  }),
});

export const collections = { blog, changelog, docs, modules, caseStudies, comparisons };
