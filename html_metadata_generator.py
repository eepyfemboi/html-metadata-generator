"""
LICENSE
===================================================
# Sleepy's Open Source License v1.3 (OSLv1.3)

**1. Permission to Use, Modify, and Redistribute**  
Permission is hereby granted to use, modify, and redistribute the code ("Software"), provided that any modified versions of the Software are distributed under the same terms as this license.

**2. Attribution and Notification**  
Any individual or organization using, modifying, or redistributing the Software, in whole or in part, must provide clear notification that the Software is being used and must include a link to a relevant webpage or repository associated with the Software, if such a webpage or repository exists. If no such webpage or repository exists, this requirement is waived.

**3. Profit Sharing**  
Any individual or organization that generates revenue or profit from the use, modification, or redistribution of the Software, in whole or in part, is required to share 30% of the profits with the owner of the Software, provided that the total generated profit for a given payment period exceeds $100. Payments must be made on a quarterly basis, accompanied by a financial report detailing the revenue and profit generated from the Software. If the profit that would be collected by the original author is less than $30, the user is exempt from these terms for that period.

**4. Revocation of Rights**  
The owner of the Software reserves the right to revoke any individual's or organization's permission to use, modify, or redistribute the Software at any time, for any reason or no reason at all. Upon revocation, the individual or organization must cease all use, modification, and redistribution of the Software.

**5. Creator Exemption Clause**  
The creator of this license may exempt and/or un-exempt themselves from any terms of the license at any time and for any reason.

**6. Author's Rights to Modified Code**  
The author of the Software retains the right to use any code from modified versions of the Software in any way, without the knowledge or consent of the user who created the modified version.

**7. Scope of Terms**  
The terms outlined in this license apply to individuals or organizations that use the Software as part of their own products, not to end users of those products.

**8. Contact Requirement**  
Anyone using, modifying, or redistributing the Software must provide a valid contact method.

**9. Prohibition of Malicious Use**  
The Software, including any modified or redistributed versions, may not be used for any malicious purposes or in any way that could cause harm to any individual, organization, system, or entity. Malicious purposes include, but are not limited to, unauthorized access to systems, data breaches, distribution of malware, denial-of-service attacks, or any activity intended to exploit, damage, or disrupt services, devices, or personal safety.

**10. Legal Enforcement**  
The author of the Software reserves the right to take legal action, including but not limited to DMCA takedown notices, against anyone who violates the terms of this license.

**11. Disclaimer of Warranties and Liability**  
The Software is provided "as-is," without warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement. In no event shall the owner of the Software be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the Software or the use or other dealings in the Software.
===================================================
"""


from typing import List, Literal
import html


class HTMLMetadataTags:
    def __init__(self,
                 title: str = None,
                 description: str = None,
                 keywords: List[str] = None,
                 url: str = None,
                 site_name: str = None,
                 image: str = None,
                 audio: str = None,
                 video: str = None,
                 canonical: str = None,
                 twitter_card: Literal["summary", "summary_large_image"] = "summary",
                 twitter_creator: str = "@eepyfemboi",
                 twitter_site: str = "@eepyfemboi"
                ):
        self.title: str = title
        self.description: str = description
        self.keywords: List[str] = keywords
        self.url: str = url
        self.site_name: str = site_name
        self.image: str = image
        self.audio: str = audio
        self.video: str = video
        self.canonical: str = canonical
        if twitter_site is not None and not twitter_site.startswith("@"):
            twitter_site = "@" + twitter_site
        if twitter_creator is not None and not twitter_creator.startswith("@"):
            twitter_creator = "@" + twitter_creator
        self.twitter_site: str = twitter_site
        self.twitter_creator: str = twitter_creator
        self.twitter_card: Literal["summary", "summary_large_image"] = twitter_card if twitter_card is not None and twitter_card in ["summary", "summary_large_image"] else "summary"

    def convert_to_html(self) -> str:
        output = f"""<!-- Default Tags -->\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<meta property="og:type" content="website">\n<meta name="twitter:card" content="{self.twitter_card}">"""
        if self.title:
            title = html.escape(self.title, quote=True)
            output += f"""\n\n<!-- Titles -->\n<title>{title}</title>\n<meta name="pagename" content="{title}">\n<meta property="og:title" content="{title}">\n<meta name="twitter:title" content="{title}">"""
        if self.description:
            description = html.escape(self.description, quote=True)
            output += f"""\n\n<!-- Descriptions -->\n<meta name="description" content="{description}">\n<meta property="og:description" content="{description}">\n<meta name="twitter:description" content="{description}">"""
        if self.keywords:
            keywords = html.escape(", ".join(self.keywords), quote=True)
            output += f"""\n\n<!-- Keywords -->\n<meta name="keywords" content="{keywords}">\n<meta name="news_keywords" content="{keywords}">"""
        if any(self.url, self.canonical, self.site_name, self.twitter_site, self.twitter_creator):
            output += f"""\n\n<!-- Site Data -->"""
            if self.url:
                output += f"""\n<meta name="url" content="{self.url}">\n<meta property="og:url" content="{self.url}">\n<meta name="twitter:url" content="{self.url}">"""
            if self.canonical:
                output += f"""\n<link rel="canonical" href="{self.canonical}">"""
            if self.site_name:
                output += f"""\n<meta property="og:site_name" content="{self.site_name}">"""
            if self.twitter_site:
                output += f"""\n<meta name="twitter:site" content="{self.twitter_site}">"""
            if self.twitter_creator:
                output += f"""\n<meta name="twitter:creator" content="{self.twitter_creator}">"""
        if any(self.image, self.audio, self.video):
            output += """\n\n<!-- Media -->"""
            if self.image:
                output += f"""\n<meta property="og:image" content="{self.image}">\n<meta name="twitter:image" content="{self.image}">"""
            if self.audio:
                output += f"""\n<meta property="og:audio" content="{self.audio}">"""
            if self.video:
                output += f"""\n<meta property="og:video" content="{self.video}">"""

        return output


def generate_html_metadata(
        title: str = None,
        description: str = None,
        keywords: List[str] = None,
        url: str = None,
        site_name: str = None,
        image: str = None,
        audio: str = None,
        video: str = None,
        canonical: str = None,
        twitter_card: Literal["summary", "summary_large_image"] = "summary",
        twitter_creator: str = "@eepyfemboi",
        twitter_site: str = "@eepyfemboi"
    ) -> str:
    return HTMLMetadataTags(title, description, keywords, url, site_name, image, audio, video, canonical, twitter_card, twitter_creator, twitter_site).convert_to_html()
