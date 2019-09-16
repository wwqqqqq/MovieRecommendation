# Movie Recommendation System

## Strategy

1. Retrieve data from online movie database.
    * Each movie has a unique TT Id and each crew member has a NM Id.
    * Besides movie information, select a group of top reviewers and get their raking on movies in database.
        - Each user has a unique UR Id on IMDb.
2. Create a recommendation system that allows users to like or dislike several movies and tries to recommend movies for them.

## TODO
- [x] Find some movie lists.
  - [Top 100 Greatest Movies of All Time](https://www.imdb.com/list/ls055592025/)
  - [IMDb Top 250](https://www.imdb.com/chart/top)
  - [IMDb Top 250 (By popularity)](https://www.imdb.com/search/title/?groups=top_250)
  - [Highest Grossing Movies Worldwide](https://www.imdb.com/list/ls063528769/)
  - [Top 50 Action Movies](https://www.imdb.com/list/ls069349708/)
  - [Best Sci-fi Movies](https://www.imdb.com/list/ls025899454/)
  - [Best Romance Movies](https://www.imdb.com/list/ls025828574/)
  - [Best Comedy Movies](https://www.imdb.com/list/ls072723591/)
  - [Best Adventure Movies](https://www.imdb.com/list/ls069375441/)
  - [Best Thriller Movies](https://www.imdb.com/list/ls058238715/)
  - [Best Fantasy Movies](https://www.imdb.com/list/ls057227085/)
- [ ] Get all movie links from the lists.
  - Exclude movies that has rating count less than 50,000.
- [x] Extract movie information from an IMDb page.
- [ ] Get IMDb's top reviewers and get their rating history.
- [ ] Write the filter to recommend movies based on user's rating history.


## Useful information about a movie:
- ID：tt1375666
  * `https://www.imdb.com/title/tt1375666/`
- Name: Inception
  * `#title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > h1`
- Duration: 148 min
  * `#title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > div > time`
- MPAA: PG-13
  * `#title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > div`
- Genres: Action，Adventure，Sci-fi
  * `#title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > div > a:nth-child(4)`
  * `#title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > div > a:nth-child(5)`
  * `#title-overview-widget > div.vital > div.title_block > div > div.titleBar > div.title_wrapper > div > a:nth-child(6)`
- Release Year: 2010
  * `#titleYear > a`
```html
<div class="title_wrapper">
    <h1 class="">Inception&nbsp;<span id="titleYear">(<a href="/year/2010/?ref_=tt_ov_inf">2010</a>)</span></h1>
    <div class="subtext">
            PG-13
        <span class="ghost"> </span>                    
        <time datetime="PT148M">2h 28min</time>
        <span class="ghost">|</span>
        <a href="/search/title?genres=action&amp;explore=title_type,genres&amp;ref_=tt_ov_inf">Action</a>, 
        <a href="/search/title?genres=adventure&amp;explore=title_type,genres&amp;ref_=tt_ov_inf">Adventure</a>, 
        <a href="/search/title?genres=sci-fi&amp;explore=title_type,genres&amp;ref_=tt_ov_inf">Sci-Fi</a>
        <span class="ghost">|</span>
        <a href="/title/tt1375666/releaseinfo?ref_=tt_ov_inf" title="See more release dates">16 July 2010 (USA)
        </a>            
    </div>
</div>
```
- Rating：8.8
  * `<span itemprop="ratingValue">8.8</span>`
  * `#title-overview-widget > div.vital > div.title_block > div > div.ratings_wrapper > div.imdbRating > div.ratingValue > strong > span`
- Rating Count: 1,870,457
  * `<a href="/title/tt1375666/ratings?ref_=tt_ov_rt"><span class="small" itemprop="ratingCount">1,870,457</span></a>`
  * `#title-overview-widget > div.vital > div.title_block > div > div.ratings_wrapper > div.imdbRating > a > span`
- Male Rating: 8.8
  * https://www.imdb.com/title/tt1375666/ratings
  * `#main > section > div > table:nth-child(14) > tbody > tr:nth-child(3) > td:nth-child(2) > div.bigcell`
- Female Ratings: 8.6
  * https://www.imdb.com/title/tt1375666/ratings
  * `#main > section > div > table:nth-child(14) > tbody > tr:nth-child(4) > td:nth-child(2) > div.bigcell`
- 18-29 Ratings: 9.0
  * https://www.imdb.com/title/tt1375666/ratings
  * `#main > section > div > table:nth-child(14) > tbody > tr:nth-child(2) > td:nth-child(4) > div.bigcell`
- 10 stars rating ratio
  * https://www.imdb.com/title/tt1375666/ratings
  * `#main > section > div > table:nth-child(7) > tbody > tr:nth-child(2) > td:nth-child(2) > div.allText > div`
- 1 star rating ratio
  * https://www.imdb.com/title/tt1375666/ratings
  * `#main > section > div > table:nth-child(7) > tbody > tr:nth-child(11) > td:nth-child(2) > div.allText > div`
- Director: Christopher Nolan
  * `#title-overview-widget > div.plot_summary_wrapper > div.plot_summary > div:nth-child(2)`
    * `#title-overview-widget > div.plot_summary_wrapper > div.plot_summary > div:nth-child(2) > a`
- Writer: Christopher Nolan
  * `#title-overview-widget > div.plot_summary_wrapper > div.plot_summary > div:nth-child(3)`
    * `#title-overview-widget > div.plot_summary_wrapper > div.plot_summary > div:nth-child(3) > a`
- Stars: Lenoardo DiCaprio, Joseph Gordon-Levitt, Ellen Page
  * `#title-overview-widget > div.plot_summary_wrapper > div.plot_summary > div:nth-child(4)`
    * `#title-overview-widget > div.plot_summary_wrapper > div.plot_summary > div:nth-child(4) > a:nth-child(2)`
    * `#title-overview-widget > div.plot_summary_wrapper > div.plot_summary > div:nth-child(4) > a:nth-child(3)`
    * `#title-overview-widget > div.plot_summary_wrapper > div.plot_summary > div:nth-child(4) > a:nth-child(4)`
```html
<div class="plot_summary ">
    <div class="summary_text">
        A thief who steals corporate secrets through the use of dream-sharing technology is given the inverse task of planting an idea into the mind of a C.E.O.
    </div>

    <div class="credit_summary_item">
        <h4 class="inline">Director:</h4>
        <a href="/name/nm0634240/?ref_=tt_ov_dr">Christopher Nolan</a>
    </div>
    <div class="credit_summary_item">
        <h4 class="inline">Writer:</h4>
        <a href="/name/nm0634240/?ref_=tt_ov_wr">Christopher Nolan</a>
    </div>
    <div class="credit_summary_item">
        <h4 class="inline">Stars:</h4>
        <a href="/name/nm0000138/?ref_=tt_ov_st_sm">Leonardo DiCaprio</a>, <a href="/name/nm0330687/?ref_=tt_ov_st_sm">Joseph Gordon-Levitt</a>, <a href="/name/nm0680983/?ref_=tt_ov_st_sm">Ellen Page</a>
        <span class="ghost">|</span>
        <a href="fullcredits/?ref_=tt_ov_st_sm">See full cast &amp; crew</a>&nbsp;»
    </div>
</div>
```
- Metascore: 74
  * `<div class="metacriticScore score_favorable titleReviewBarSubItem"><span>74</span></div>`
  * `#title-overview-widget > div.plot_summary_wrapper > div.titleReviewBar > div:nth-child(1) > a > div > span`
- Keywords: dream, subconscious, ambiguous ending, thief, psycho thriller
  * `#titleStoryLine > div:nth-child(6)`
    * `#titleStoryLine > div:nth-child(6) > a:nth-child(2) > span`
    * `#titleStoryLine > div:nth-child(6) > a:nth-child(4) > span`
    * etc.
```html
<div class="see-more inline canwrap">
    <h4 class="inline">Plot Keywords:</h4>
    <a href="/search/keyword?keywords=dream&amp;ref_=tt_stry_kw"> <span class="itemprop">dream</span></a>
    <span>|</span>
    <a href="/search/keyword?keywords=subconscious&amp;ref_=tt_stry_kw"> <span class="itemprop">subconscious</span></a>
    <span>|</span>
    <a href="/search/keyword?keywords=ambiguous-ending&amp;ref_=tt_stry_kw"> <span class="itemprop">ambiguous ending</span></a>
    <span>|</span>
    <a href="/search/keyword?keywords=thief&amp;ref_=tt_stry_kw"> <span class="itemprop">thief</span></a>
    <span>|</span>
    <a href="/search/keyword?keywords=psycho-thriller&amp;ref_=tt_stry_kw"> <span class="itemprop">psycho thriller</span></a>
    <span>|</span>&nbsp;<nobr><a href="/title/tt1375666/keywords?ref_=tt_stry_kw">See All (346)</a>&nbsp;»</nobr>
</div>
```
- Taglines: Your mind is the scene of the crime
  * `#titleStoryLine > div:nth-child(8)`
```html
<div class="txt-block">
    <h4 class="inline">Taglines:</h4>
    Your mind is the scene of the crime                
    <span class="see-more inline">
        <a href="/title/tt1375666/taglines?ref_=tt_stry_tg"> See more</a>&nbsp;»
    </span>
</div>
```           
- Production: WB
  * `<a href="/company/co0025059?ref_=cons_tt_dt_co_1"> Warner Bros.</a>`
  * `#titleDetails > div:nth-child(19) > a:nth-child(2)`
- Worldwide Gross: \$829,895,144
  * `#titleDetails > div:nth-child(15)`
```html
<div class="txt-block">
    <h4 class="inline">Cumulative Worldwide Gross:</h4> $829,895,144        
</div>
```
- Budget: \$160,000,000
  * `#titleDetails > div:nth-child(12)`
```html
<div class="txt-block">
    <h4 class="inline">Budget:</h4>$160,000,000
    <span class="attribute">(estimated)</span>
</div>
```