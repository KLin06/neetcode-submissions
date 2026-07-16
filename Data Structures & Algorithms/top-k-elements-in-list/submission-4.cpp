class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        int length = nums.size();
        map <int, int> charFreq;

        for (int i = 0; i < length; i++){
            charFreq[nums[i]]++;
        }

        vector <vector<int>> buckets(length);
        for (auto item: charFreq){
            buckets[item.second - 1].push_back(item.first);
        }

        vector <int> sol;

        for(int i = length - 1; i >= 0; i--){
            for(int n: buckets[i]){
                sol.push_back(n);

                if(sol.size() == k)
                    return sol;
            }
        }
        return sol;



        
    }
};
