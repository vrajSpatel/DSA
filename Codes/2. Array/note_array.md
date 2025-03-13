--> how array element stored in memory?
    -> always in continues memory

    1. 1D array :
        - in this type of array it is stored in continues memory 
        - example :
            [1,2,3,4,5,6]  -> 1 2 3 4 5 6 (in memory)

    2. Multi-dimensinonal array :
        - in this also it stored in continues memory but store element in row to row
        - example :

            1. 2D array :
                [ [1,2,3] , [5,6,7] , [9,10,11] ] -> 1 2 3 5 6 7 9 10 11

            2. 3D array :
                [
                    [ [1,2,3] , [4,5,6] ] 
                    [ [7,8,9] , [10,11,12] ]
                    [ [13,14,15] , [16,17,18] ]
                ]
                    it store like -> 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18

--> Insertion of element in array :
    1. insert at start 
    2. insert at end
    3. insert at middle

    -> time complexcity will be O(n)

--> Traversal in array :
    - using for loop

--> Access the element of array :
    -with the index of each element

--> Finding the element in array :
    -using for loop and if condition

--> Deletion of element in array :
    1. delete at start 
        - time complexcity will be o(n)
    2. delete at end 
        - time complexcity will be o(1)
    3. delete at middle
        - time complexcity will be o(n)
    
    - we use remove() function to delete elemtent in array

--> Update the element in array :
    -using index of element and assign new value to it



---> 2 D array
 - here we use numpy module because it is very easy to use and have many function to use