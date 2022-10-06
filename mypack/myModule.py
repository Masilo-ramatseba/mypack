def top_n(items, n):
    """ Return the top items in an array, in desc order.

    Args:
        items (array): list or array-like object
        n (int) the number of items ,in desc order

    Return:
        Egs:
            >>> top_n([8,3,2,7,4])
            [8,7,3]
        """
    for i in range(n): #keep sorting until we have the top n items
        for j in range(len(items)-1-i):

            if items[j] > items[j+1]:   #if this item is begger than the next item..
                items[j], items[j+1] =items[j+1], items[j]  #swap the two
    # get the last iems
    top_n = items[-n: ]       

    #return in descending order
    return top_n[::-1]     
