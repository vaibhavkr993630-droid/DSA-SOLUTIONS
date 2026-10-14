class Solution {
public:
    vector<int> arrayRankTransform(vector<int>& arr) {
        vector<int> neww=arr;
        sort(neww.begin(),neww.end());

        neww.erase(unique(neww.begin(), neww.end()), neww.end());
        
        unordered_map<int,int> mp;
        for(int i=0;i<neww.size();i++)
            mp.insert({neww[i],i+1});
        
        for(int i=0;i<arr.size();i++){
            arr[i]=mp.find(arr[i])->second;
        }
        return arr;
    }
};