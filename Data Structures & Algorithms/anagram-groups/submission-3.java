class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        int[][] list = new int[26][strs.length];
        boolean[] checked = new boolean[strs.length];

        for(int i = 0 ; i < strs.length; i++){
            for(int j = 0; j < strs[i].length(); j++){
                list[strs[i].charAt(j) - 'a'][i]++;
            }
        }

        List<List<String>> anagrams = new ArrayList<>();
        for(int i = 0; i < strs.length; i++){
            if(!checked[i]){
                ArrayList<String> tempList = new ArrayList<>();
                tempList.add(strs[i]);

                for(int j = i + 1; j < strs.length; j++){
                    if(!checked[j]){
                        boolean sameAsI = true;
                        for(int k = 0; k < 26; k++){
                            if(list[k][i] != list[k][j]){
                                sameAsI = false;
                                break;
                            }
                        }
                        if(sameAsI){
                            checked[j] = true;
                            tempList.add(strs[j]);
                        }
                    }
                }
                anagrams.add(tempList);
            }
        }


        return anagrams;
    }
}


