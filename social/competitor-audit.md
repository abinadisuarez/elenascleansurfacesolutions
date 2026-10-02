# Competitor and Benchmark Audit (TikTok, public data, 2026-10-02)

## Method and limits
- Public TikTok profile and video pages fetched with `curl` (no login, no private APIs). Profile pages give bio, link, followers, videos, total likes. A single video page gives plays, likes, comments, shares, saves, duration, date, caption.
- Videos were found through web search, so this is a **small, non-random sample of videos that search engines surfaced** (survivorship bias: popular posts are over-represented). Treat percentages as rough benchmarks, not norms.
- Instagram and Facebook competitor pages are login-walled or blocked from this environment, so **no Instagram/Facebook competitor data is included** (unverified). Competitor websites were also unreachable.
- Account-level numbers are a snapshot; I could not list each account's full recent feed, so posting cadence per account is **unverified** except where stated.

## 1. Local competitors that cover Elena's service area (primary focus)
Elena's area (per website): Nashville, Murfreesboro, Smyrna, La Vergne, Franklin, Mount Juliet, Lebanon, Clarksville.

**Access reality:** Facebook returns a login wall or HTTP 400 to logged-out `curl` (checked on 8 competitor pages), Instagram returns 429/login, and competitor websites reset the connection. Everything below about Facebook/Instagram/websites therefore comes from **search-result descriptions** (copied facts, not my review of their feeds). Their posting cadence, formats, post engagement and offers on social are **unverified**. TikTok was the only platform I could read directly.

| Competitor | Overlap with Elena's area | Services / positioning (from search text) | Social presence found | Offer / price signal |
|---|---|---|---|---|
| Murfreesboro Chem-Dry | Murfreesboro, Smyrna, La Vergne, Nashville, Franklin | Residential + commercial carpet and upholstery; family owned since 2006; Hot Carbonating Extraction (fast dry) | Social accounts not found | None found |
| Mr. B's Chem-Dry | Smyrna, La Vergne, Murfreesboro | Carpet, rug, tile, upholstery | Not found | None found |
| Safe-Dry Carpet Cleaning (Murfreesboro and Mt. Juliet franchises) | Murfreesboro, Smyrna, Mt. Juliet, Lebanon | Hypoallergenic carpet, upholstery, tile, hardwood; about 1 hour dry; "open 24/7" | Facebook (`1800safedry`: 50% recommend, 8 reviews per snippet) and Instagram (`@safedrycarpetcleaning`, per search snippet) | **"3 Rooms $88"** shown on titles |
| Safe Solutions Carpet Cleaning | Murfreesboro, Smyrna, Franklin, Brentwood | Local, family owned | Facebook (100% recommend, 12 reviews) and Instagram (per snippet) | None found |
| Steem Master of Murfreesboro | Murfreesboro | Family owned; "premium fabric and floor care" | Facebook (100% recommend, 31 reviews) | None found |
| Carpet Docs | Murfreesboro (and Smyrna area) | Carpet and upholstery, same-day service, 10+ years, "honest pricing" | Not found | "Honest pricing" claim |
| Industrial Carpet & Upholstery Cleaning | Murfreesboro, Smyrna, La Vergne, Franklin, Lebanon, Mt. Juliet | Carpet, upholstery, tile | Not found | None found |
| Clean N Go Carpet Cleaning | Smyrna | Local | Facebook (`Cleango817`) | Unknown |
| The Shine Carpet Cleaning LLC | Smyrna (Sam Ridley Pkwy) | Local | Facebook (`TheShinecarpetclening`) | Unknown |
| Mac Carpet Care | Smyrna | "Honest and affordable" | Not found | "Affordable" claim |
| EverClean Nashville | Nashville, Franklin, Clarksville, Mt. Juliet | IICRC certified; since 2009; SaniVive steam plus low-moisture method; non-toxic; A+ BBB | Facebook, Instagram, YouTube, Pinterest, Medium, Nextdoor; 51 Yelp reviews (July 2026, per snippet) | "615-DRY-FAST" phone hook |
| Nashville Carpet Cleaning | Nashville / Middle TN | Carpet, upholstery, rugs, vehicle, mattress (closest to Elena's mix) | Instagram `@nashvillecarpetcleaning` about 430 followers (search snippet, unverified); Facebook page | Before/after images on website |
| Nashville Carpet Care | Nashville and surrounding | Residential and commercial carpet, rug, tile, upholstery, window | Facebook with before/after posts (per snippet) | None found |
| Carpetmaster | Nashville | 25+ years; residential, commercial, government | Facebook (reviews page exists) | None found |
| Zerorez, Oxi Fresh, Stanley Steemer, MasterClean of Mt. Juliet | Nashville, Mt. Juliet, Lebanon, Smyrna | National brands / 25+ year local firm | Facebook for Stanley Steemer; others unverified | Not collected |

**TikTok (verified by direct fetch):**
- No competitor above has a meaningful TikTok account I could confirm. Guessing handles mostly returned unrelated accounts, so I did **not** attribute them.
- Two possible local handles: `@evercleannashville` (6 followers, 2 videos, 2 likes) and `@nashvillecarpetcleaning` (0 videos). Whether they are the companies' official accounts is **unverified**.
- Conclusion: local TikTok is effectively empty. Elena's (6 followers, 10 videos) is at least level with the only local accounts found.

**Local patterns visible in public text (not feed analysis):**
1. **Reviews are the local currency.** Where review counts are visible they are small: 8, 12, 31 on Facebook, 51 on Yelp (EverClean). A steady flow of 4+ reviews a month would put Elena's in the range of the Murfreesboro field within a few months, if Elena's has reviews at all (unverified).
2. **Trust claims repeated:** years in business (since 2006, 2009, 10+, 25+), IICRC certification, family owned, non-toxic/hypoallergenic, fast dry. Elena's site says "licensed and insured" and "fast dry" but no years or certification (confirm with owner).
3. **Price anchors:** only Safe-Dry shows a number ("3 rooms $88"); most others say "honest/affordable". A concrete example price would stand out.
4. **Availability hooks:** "same-day" (Carpet Docs), "open 24/7" (Safe-Dry), Sunday hours (Chem-Dry). Elena's is closed Sunday.
5. **Elena's gaps vs. the field:** no testimonials, no gallery, no price, no years/certification on the site. Elena's strengths vs. this list: mattress + upholstery + auto interior and commercial floors together, and a stated five-step process.
6. **Closest direct rival by service mix:** Nashville Carpet Cleaning (carpet, upholstery, rugs, vehicle, mattress). Check its Instagram first when screenshots are possible.

### 1b. Instagram: local competitors (search-snippet level)
**Access:** Instagram redirects logged-out `curl` to login (HTTP 429/302), so I did not read any feed and did not try to bypass it. The numbers below are follower/following/post counts that web search shows in each profile's description. They are **cached snapshots of unknown date**, may be out of date, and say nothing about content, cadence or engagement (all **unverified**). Elena's own `@elenasclean` returned no search results at all (likely not indexed; counts unverified).

| Instagram account | Followers | Following | Posts | Relevance to Elena's area / services (per snippet) |
|---|---|---|---|---|
| @patriotcleaningtn (Patriot Cleaning) | 3,769 | n/a | n/a | Carpets, upholstery, vehicles, soft/power washing; Middle TN (Clarksville/Mt. Juliet side) |
| @karitascleaningservice (Karita's Cleaning) | 1,833 | 288 | 1,155 | Nashville and Murfreesboro; general cleaning, not carpet-only |
| @zeroreznashville (Zerorez Nashville) | 601 | 212 | 725 | National brand franchise, Nashville |
| @anderson_carpet_cleaning | 610 | 609 | 54 | Carpet cleaning, Nashville area |
| @nashvillecarpetcleaning | 430 | 397 | 5 | Carpet, upholstery, rugs, vehicle interiors, mattresses (closest service mix) |
| @bcleancarpetllc (B Clean Carpet and Upholstery) | 268 | 430 | 54 | Carpet and upholstery |
| @safedrycarpetcleaning (Safe-Dry) | 249 | n/a | n/a | "All-natural" carpet, rugs, upholstery; franchise with Murfreesboro/Mt. Juliet locations |
| @masterfulcarpetcleaning | 164 | 185 | 73 | Carpet cleaning |
| @the_shine_carpet_cleaning_llc | 71 | 196 | 31 | Smyrna (Sam Ridley Pkwy) |
| @mrbscarpetfloorcleaning (Mr. B's) | 21 | 5 | 37 | Smyrna/Murfreesboro/La Vergne |
| @carpetcleaningdudes | n/a | n/a | n/a | Nashville, Brentwood, Franklin; carpet, rug, upholstery, tile; phone in listing |
| @nbfloorcare (Nashville's best floor care and restoration) | n/a | n/a | n/a | Floor care and restoration |
| @thomas_restoration | n/a | n/a | n/a | Restoration, Clarksville, 34+ years |

What this supports (and what it doesn't):
- **Verified from the snippets:** local carpet and upholstery competitors on Instagram are small. Most are under 700 followers; the carpet-focused ones range from 21 to about 3,800. No local carpet specialist found is large.
- Post counts vary widely: 5 posts (430 followers), 31-73 posts for small shops, 725 for Zerorez. A 430-follower account with 5 posts shows followers alone are not a sign of active content.
- **Opportunity:** a consistent account with real before/after Reels (3 per week) would out-post nearly all of these within a few months. This is an inference from counts only; I could not see whether their posts are Reels, photos or reposts.
- **Not verified:** engagement per post, formats, captions, hashtags, local tags, highlights, link in bio, offers. These need screenshots.
- Account-level caution: this list mixes carpet specialists and general cleaning companies (Karita's, Maid in America, Concierge Cleaners are not direct competitors).

**To finish Instagram properly (needs you):** open each handle above while logged in and send screenshots of the profile header and the last 9-12 posts (or tell me the view/like counts). Priority order: @nashvillecarpetcleaning, @patriotcleaningtn, @zeroreznashville, @safedrycarpetcleaning, @anderson_carpet_cleaning. Also send Elena's own `@elenasclean` header, grid and Insights.

## 2. Small professional cleaners elsewhere (content-pattern benchmarks only; not local competitors)
| Account | Where | Followers | Videos | Likes | Bio / link |
|---|---|---|---|---|---|
| @mrlightningcarpet | Melbourne, AU (per search result) | 7,708 | 335 | 310,700 | "Carpet, upholstery, Tile & Grout cleaning, Foam and Hot Water extraction method"; no link |
| @jccarpetcleaning | Kent/Surrey/Sussex, UK | 3,015 | 159 | 53,600 | Service area in bio; no link |
| @cleanwithclick | Los Angeles | 1,667 | 59 | 26,900 | "Easily book online here", **booking link** (Housecall Pro) |
| @carpetguysperth | Perth, AU | 1,320 | 100 | 17,500 | "Eco-friendly & family safe, BOOK NOW" plus Facebook link |
| @oxymagiccarpetcleaning | Blaine, MN | 520 | 299 | 17,700 | City, "Green Seal Certified", phone, website in bio |
| @steampro.carpetcleaning | Chilliwack, BC | 356 | 280 | 3,250 | Lists towns served; no link |

Patterns:
- **Bios that convert** name the city or service area and one trust claim, then give a booking link, phone or website (`@cleanwithclick`, `@oxymagiccarpetcleaning`, `@carpetguysperth`). Elena's bio has none of these.
- **Volume matters more than polish for small accounts.** The accounts that built a likes base posted 100-335 videos (`@mrlightningcarpet`, `@oxymagiccarpetcleaning`, `@steampro`); Elena's has 10. Likes per video (rough, total likes / videos): mrlightningcarpet about 930, jccarpetcleaning about 340, cleanwithclick about 460, carpetguysperth about 175, Elena's 3.5. These averages are skewed by a few hits.
- Service lists in bios match Elena's: "Carpet, upholstery, tile & grout" is the same trio, and mrlightningcarpet names the method ("foam and hot water extraction"). Confirms keeping tile and grout in the bio, if offered.

## 3. Viral and high-performing videos (sample of 11, verified numbers)
| Video | Date | Length | Plays | Likes | Comments | Shares | Saves | Like/view | Save/view |
|---|---|---|---|---|---|---|---|---|---|
| @mountainrugcleaning, "Disgustingly Filthy Cotton Rug Cleaned In 60 Seconds! Satisfying ASMR" | 2023-07 | 58s | 10.7M | 295.4K | 1,431 | 17.9K | 19.1K | 2.8% | 0.18% |
| @mountainrugcleaning, "A Minute of Magic: Witness the Incredible Transformation of This Filthy Rug!" | 2023-04 | 59s | 11.1M | 422.0K | 2,381 | 9.1K | 28.8K | 3.8% | 0.26% |
| @mountainrugcleaning, "This Rug Had A CRAZY Amount Of Dirt On It..." | 2024-09 | 118s | 4.4M | 71.7K | 759 | 2.5K | 2.0K | 1.6% | 0.05% |
| @kaelyngutierrez, "Deep cleaning my living room carpet" (homeowner, not a business) | 2025-05 | 164s | 5.6M | 792.3K | 1,274 | 6.3K | 20.9K | 14.2% | 0.37% |
| @_amanduhh__, "Should I have done another pass through?" (homeowner) | 2025-03 | 83s | 1.7M | 122.5K | 1,018 | 1.3K | 2.9K | 7.2% | 0.17% |
| @jeeves_ny, "How to remove a pee stain from a mattress / furniture" | 2022-12 | 39s | 265.9K | 7.4K | 45 | 348 | 1.6K | 2.8% | 0.61% |
| @zoelovestoclean, mattress stain remover test | 2024-03 | 41s | 198.4K | 1.2K | 106 | 84 | 188 | 0.6% | 0.09% |
| @wirecutter, "we cleaned a filthy old rug on the sidewalk" | 2024-08 | 51s | 24.5K | 791 | 13 | 70 | 214 | 3.2% | 0.87% |
| @jccarpetcleaning, "Bit of stain removal" (pro) | 2025-05 | 201s | 2.0K | 90 | 1 | 1 | 18 | 4.5% | 0.90% |
| @kpa.upholstery, mattress cleaning (pro, South Africa) | 2026-04 | 32s | 3.9K | 86 | 13 | 11 | 16 | 2.2% | 0.41% |
| @cleanwithclick, "Expert cleaning... Fast booking" (pro) | 2025-05 | 36s | 4.8K | 38 | 3 | 5 | 7 | 0.8% | 0.15% |

What the numbers do and don't support:
- **Verified:** the mega-hits (4-11M plays) are all "dirty thing becomes clean" visuals shown in one continuous take, about 1 minute (58-59s), with a numbers-and-superlative title ("Disgustingly Filthy", "CRAZY Amount Of Dirt", "In 60 Seconds") and 4-7 niche tags (#asmr #carpetcleaning #satisfying #oddlysatisfying #restoration).
- **Verified:** the two highest like-rates came from homeowner-style, longer "cleaning with me" videos (14% and 7%), not from branded business posts. Branded service ads (`@cleanwithclick`, `@kpa.upholstery`) sit at roughly 4-5K views.
- **Verified:** professional local-style posts get a few thousand views at best (2.0K-6.3K in this sample). A hit is not the typical outcome.
- **Not supported:** that these videos generated leads. None of the viral accounts is a local-lead model: `@mountainrugcleaning` (3.1M followers) now uses its bio to promote a mobile game, so it is a content business, not a service benchmark; its audience is not Middle Tennessee.
- **Unverified:** hashtag reach, posting times, sound use, and whether hashtag-stuffed captions help. `@jccarpetcleaning` used about 30 hashtags and got 2.0K views, so more tags are not evidently better.

## 4. Patterns to adopt (and what to ignore)
Adopt:
1. **One-take transformation, 30-60 seconds**, single angle, no cuts, ending on the clean stripe or full reveal. Capture the sound (ASMR is in nearly every hit).
2. **Title formula:** [extreme adjective] + [item] + [result/time]. E.g. "This Smyrna couch hadn't been cleaned in 10 years."
3. **4-6 hashtags:** 2 broad (#carpetcleaning, #satisfying), 2-3 local (#smyrnatn, #nashvillecleaning).
4. **Bio = city + service list + trust claim + one way to book**, as the best small pros do.
5. **Volume:** the small accounts that built traction posted 100+ videos. Target 3 per week, reusing the same job for TikTok, Reels and Facebook.
6. **Homeowner-style "clean with me"** longer (80-160s) format as a secondary test, since the highest like-rates came from it.

Ignore or adapt:
- Monetization-driven accounts (mega rug channels) and 30-hashtag captions.
- Anything that needs a national audience. Local likes and a booking path matter more than views from outside the service area.

## 5. Still to do (needs data I cannot reach)
- Instagram content analysis (section 1b has counts only) and Facebook audit of the local competitors in section 1 (cadence, formats, offers, reviews): needs screenshots or a logged-in session. Suggested priority: Nashville Carpet Cleaning, Safe-Dry (Murfreesboro/Mt. Juliet), Safe Solutions, Steem Master, EverClean.
- Google Business Profile review counts and photos for each local competitor.
- Verify whether `@evercleannashville` and `@nashvillecarpetcleaning` are the companies' official accounts.
- Per-video feeds for the six benchmark accounts (to measure cadence and hit rate).

Sources are public TikTok profile and video pages and the search results listed in the session summary.
