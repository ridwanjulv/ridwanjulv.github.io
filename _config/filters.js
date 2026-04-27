import { DateTime } from "luxon";

export default function(eleventyConfig) {
	eleventyConfig.addFilter("readableDate", (dateObj, format, zone) => {
		return DateTime.fromJSDate(dateObj, { zone: zone || "utc" }).toFormat(format || "dd LLLL yyyy");
	});

	eleventyConfig.addFilter("htmlDateString", (dateObj) => {
		return DateTime.fromJSDate(dateObj, { zone: "utc" }).toFormat('yyyy-LL-dd');
	});

	eleventyConfig.addFilter("head", (array, n) => {
		if(!Array.isArray(array) || array.length === 0) { return []; }
		if( n < 0 ) { return array.slice(n); }
		return array.slice(0, n);
	});

	eleventyConfig.addFilter("min", (...numbers) => {
		return Math.min.apply(null, numbers);
	});

	eleventyConfig.addFilter("getKeys", target => {
		return Object.keys(target);
	});

	eleventyConfig.addFilter("filterTagList", function filterTagList(tags) {
		return (tags || []).filter(tag => ["all", "posts"].indexOf(tag) === -1);
	});

	eleventyConfig.addFilter("sortAlphabetically", strings =>
		(strings || []).sort((b, a) => b.localeCompare(a))
	);

	eleventyConfig.addFilter("readingTime", (content) => {
		const text = String(content).replace(/<[^>]*>/g, " ").replace(/\s+/g, " ").trim();
		const words = text ? text.split(" ").length : 0;
		return Math.max(1, Math.ceil(words / 238));
	});

	// Extract h2/h3 headings from rendered HTML for a build-time TOC.
	// IDs are generated from heading text to match what IdAttributePlugin will produce.
	eleventyConfig.addFilter("toc", (content) => {
		const items = [];
		const re = /<h([23])[^>]*>([\s\S]*?)<\/h[23]>/gi;
		let match;
		while ((match = re.exec(String(content))) !== null) {
			const text = match[2].replace(/<[^>]*>/g, "").trim();
			const id = text.toLowerCase().replace(/[^\w\s-]/g, "").replace(/\s+/g, "-").replace(/-+/g, "-").replace(/^-|-$/g, "");
			items.push({
				level: parseInt(match[1], 10),
				id,
				text,
			});
		}
		return items;
	});
}
