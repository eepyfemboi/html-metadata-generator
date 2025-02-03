`
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
`


function generate_html_metadata({
    title,
    description,
    keywords,
    url,
    site_name,
    image,
    audio,
    video,
    canonical,
    twitter_card,
    twitter_creator,
    twitter_site
} = {}) {
    if (twitter_site && !twitter_site.startsWith("@")) {
        twitter_site = "@" + twitter_site;
    }
    if (twitter_creator && !twitter_creator.startsWith("@")) {
        twitter_creator = "@" + twitter_creator;
    }
    
    if (!["summary", "summary_large_image"].includes(twitter_card)) {
        twitter_card = "summary";
    }
    
    let output = `<!-- Default Tags -->\n<meta charset="UTF-8">\n<meta name="viewport" content="width=device-width, initial-scale=1.0">\n<meta property="og:type" content="website">\n<meta name="twitter:card" content="${twitter_card}">`;
    
    if (title) {
        output += `\n\n<!-- Titles -->\n<title>${title}</title>\n<meta name="pagename" content="${title}">\n<meta property="og:title" content="${title}">\n<meta name="twitter:title" content="${title}">`;
    }
    
    if (description) {
        output += `\n\n<!-- Descriptions -->\n<meta name="description" content="${description}">\n<meta property="og:description" content="${description}">\n<meta name="twitter:description" content="${description}">`;
    }
    
    if (keywords) {
        let keywords_ = Array.isArray(keywords) ? keywords.join(", ") : keywords;
        keywords_ = keywords_.trim()
        if (!keywords_ === "") {
            output += `\n\n<!-- Keywords -->\n<meta name="keywords" content="${keywords_}">\n<meta name="news_keywords" content="${keywords_}">`;
        }
    }
    
    if (url || canonical || site_name || twitter_site || twitter_creator) {
        output += `\n\n<!-- Site Data -->`;
        if (url) {
            output += `\n<meta name="url" content="${url}">\n<meta property="og:url" content="${url}">\n<meta name="twitter:url" content="${url}">`;
        }
        if (canonical) {
            output += `\n<link rel="canonical" href="${canonical}">`;
        }
        if (site_name) {
            output += `\n<meta property="og:site_name" content="${site_name}">`;
        }
        if (twitter_site) {
            output += `\n<meta name="twitter:site" content="${twitter_site}">`;
        }
        if (twitter_creator) {
            output += `\n<meta name="twitter:creator" content="${twitter_creator}">`;
        }
    }
    
    if (image || audio || video) {
        output += `\n\n<!-- Media -->`;
        if (image) {
            output += `\n<meta property="og:image" content="${image}">\n<meta name="twitter:image" content="${image}">`;
        }
        if (audio) {
            output += `\n<meta property="og:audio" content="${audio}">`;
        }
        if (video) {
            output += `\n<meta property="og:video" content="${video}">`;
        }
    }
    
    return output;
}
