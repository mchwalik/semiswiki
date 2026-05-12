import { QuartzConfig } from "./quartz/cfg"
import * as Plugin from "./quartz/plugins"

const config: QuartzConfig = {
  configuration: {
    pageTitle: "Equity Research Wiki",
    pageTitleSuffix: "",
    enableSPA: true,
    enablePopovers: true,
    analytics: null,
    locale: "en-US",
    baseUrl: "example.com",
    ignorePatterns: [
      "private",
      "templates",
      ".obsidian",
      "raw",
      "journal",
      "inbox",
    ],
    defaultDateType: "modified",
    theme: {
      fontOrigin: "googleFonts",
      cdnCaching: true,
      typography: {
        header: "Inter",
        body: "Inter",
        code: "IBM Plex Mono",
      },
      colors: {
        lightMode: {
          light: "#fcfcfb",
          lightgray: "#e7e5df",
          gray: "#b3b0a8",
          darkgray: "#5a5853",
          dark: "#1f1f1d",
          secondary: "#1e5aa8",
          tertiary: "#7d5fff",
          highlight: "rgba(30, 90, 168, 0.10)",
          textHighlight: "#fff29d",
        },
        darkMode: {
          light: "#151515",
          lightgray: "#2e2e2b",
          gray: "#62625d",
          darkgray: "#d9d6cf",
          dark: "#f5f3ef",
          secondary: "#84b6ff",
          tertiary: "#a78bfa",
          highlight: "rgba(132, 182, 255, 0.14)",
          textHighlight: "#7c6f00",
        },
      },
    },
  },
  plugins: {
    transformers: [
      Plugin.FrontMatter(),
      Plugin.CreatedModifiedDate({
        priority: ["frontmatter", "git", "filesystem"],
      }),
      Plugin.SyntaxHighlighting({
        theme: {
          light: "github-light",
          dark: "github-dark",
        },
        keepBackground: false,
      }),
      Plugin.ObsidianFlavoredMarkdown({ enableInHtmlEmbed: false }),
      Plugin.GitHubFlavoredMarkdown(),
      Plugin.TableOfContents(),
      Plugin.CrawlLinks({ markdownLinkResolution: "shortest" }),
      Plugin.Description(),
      Plugin.Latex({ renderEngine: "katex" }),
    ],
    filters: [Plugin.RemoveDrafts()],
    emitters: [
      Plugin.AliasRedirects(),
      Plugin.ComponentResources(),
      Plugin.ContentPage(),
      Plugin.FolderPage(),
      Plugin.TagPage(),
      Plugin.ContentIndex({
        enableSiteMap: true,
        enableRSS: true,
      }),
      Plugin.Assets(),
      Plugin.Static(),
      Plugin.Favicon(),
      Plugin.NotFoundPage(),
      Plugin.CustomOgImages(),
    ],
  },
}

export default config
