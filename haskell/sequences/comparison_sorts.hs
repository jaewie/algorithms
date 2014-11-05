import Data.List

-- Quick sort
qsort :: (Ord a) => [a] -> [a]
qsort [] = []
qsort (x:xs) = let le = filter (<x) xs
                   gt = filter (>x) xs
                   sm = filter (==x) xs ++ [x]
               in (qsort le) ++ sm ++ (qsort gt)

-- Merge sort
msort :: (Ord a) => [a] -> [a]
msort xs 
    | len <= 1 = xs
    | otherwise = merge (msort left) (msort right)
    where
        len = length xs
        mid = div len 2
        left = take mid xs
        right = drop mid xs


-- Insertion sort
isort :: (Ord a) => [a] -> [a]
isort [] = []
isort (x:xs) = let subresult = isort xs
                   lt = filter (<=x) subresult
                   gt = filter (>x) subresult
               in lt ++ [x] ++ gt

-- Selection sort
ssort :: (Ord a) => [a] -> [a]
ssort [] = []
ssort xs = let min = minimum xs
               mins = filter (==min) xs
               rest = filter (/=min) xs
           in mins ++ (ssort rest)

-- Helpers
merge :: (Ord a) => [a] -> [a] -> [a]
merge xs [] = xs
merge [] ys = ys
merge (x:xs) (y:ys)
    | x < y = x:(merge xs (y:ys))
    | otherwise = y:(merge (x:xs) ys)
