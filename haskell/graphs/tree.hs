data Tree a = EmptyTree | Node a (Tree a) (Tree a) deriving (Show, Read, Eq)

singleton :: a -> Tree a
singleton x = Node x EmptyTree EmptyTree

insert :: (Ord a) => a -> Tree a -> Tree a
insert x EmptyTree = singleton x
insert x (Node y left right)
    | x == y = Node x left right
    | x < y = Node y (insert x left) right
    | x > y = Node y left (insert x right)

max' :: Tree a -> a
max' (Node v left EmptyTree) = v
max' (Node v left right) = max' right

rem' :: (Ord a) => a -> Tree a -> Tree a
rem' _ EmptyTree = EmptyTree
rem' val (Node key left right)
    | val < key = Node key (rem' val left) right
    | val > key = Node key left (rem' val right)
    | left == EmptyTree = right
    | right == EmptyTree = left
    | otherwise = let m = max' left
                  in (Node m (rem' m left) right)
