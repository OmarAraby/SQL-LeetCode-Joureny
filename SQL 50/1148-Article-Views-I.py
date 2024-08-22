import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    authors_viewed_their_articls = views[views['author_id']== views['viewer_id']]
    unique_authors = authors_viewed_their_articls['author_id'].unique() # --> [7, 4]
    df= pd.DataFrame({'id':unique_authors})
    return df.sort_values(by='id')