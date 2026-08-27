import type {
	ExpressiveCodeConfig,
	LicenseConfig,
	NavBarConfig,
	ProfileConfig,
	SiteConfig,
} from "./types/config";
import { LinkPreset } from "./types/config";

export const siteConfig: SiteConfig = {
	title: "ZhaoCake's Blog",
	subtitle: "Ciallo～(∠・ω< )⌒☆",
	lang: "zh_CN",
	themeColor: {
		hue: 210,
		fixed: false,
	},
	banner: {
		enable: false,
		src: "assets/images/demo-banner.png",
		position: "center",
		credit: {
			enable: false,
			text: "",
			url: "",
		},
	},
	toc: {
		enable: true,
		depth: 2,
	},
	favicon: [
		{
			src: "/assert/zhao.png",
		},
	],
};

export const navBarConfig: NavBarConfig = {
	links: [
		LinkPreset.Home,
		LinkPreset.Archive,
		LinkPreset.About,
		{
			name: "GitHub",
			url: "https://github.com/ZhaoCake",
			external: true,
		},
	],
};

export const profileConfig: ProfileConfig = {
	avatar: "/assert/zhao.png",
	name: "ZhaoCake",
	bio: "Ciallo～(∠・ω< )⌒☆ 记录学习笔记与生活感悟",
	links: [
		{
			name: "GitHub",
			icon: "fa6-brands:github",
			url: "https://github.com/ZhaoCake",
		},
		{
			name: "Bilibili",
			icon: "fa6-brands:bilibili",
			url: "https://space.bilibili.com/1711392619",
		},
		{
			name: "Zhihu",
			icon: "fa6-brands:zhihu",
			url: "https://www.zhihu.com/people/42-48-12-1",
		},
		{
			name: "QQ",
			icon: "fa6-brands:qq",
			url: "tencent://message/?uin=2317634877&Site=&Menu=yes",
		},
	],
};

export const licenseConfig: LicenseConfig = {
	enable: true,
	name: "Apache 2.0",
	url: "https://www.apache.org/licenses/LICENSE-2.0",
};

export const expressiveCodeConfig: ExpressiveCodeConfig = {
	theme: "github-dark",
};
