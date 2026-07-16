class Solution {
    public int getBox (int row, int col){
        return 3 * (int)(row / 3) + (int)(col / 3);
    }
    public boolean isValidSudoku(char[][] board) {
        List<Set<Character>> boxes = new ArrayList<>();
        List<Set<Character>> rows = new ArrayList<>();
        List<Set<Character>> cols = new ArrayList<>();

        for (int i = 0; i < 9; i++) {
            boxes.add(new HashSet<>());
            rows.add(new HashSet<>());
            cols.add(new HashSet<>());
        }

        for(int row = 0; row < 9; row++){
            for(int col = 0; col < 9; col++){
                char val = board[row][col];
                if (val == '.')
                    continue;
                int boxIndex = getBox(row, col);
                if(boxes.get(boxIndex).contains(val) || rows.get(row).contains(val) || cols.get(col).contains(val))
                    return false;
                boxes.get(boxIndex).add(val);
                rows.get(row).add(val);
                cols.get(col).add(val);
            }
        }

        return true;
    }
}
