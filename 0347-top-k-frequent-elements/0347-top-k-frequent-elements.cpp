class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> mp;
        for(int i:nums){
            mp[i]++;
        }

        priority_queue< pair<int,int>, vector<pair<int,int>>, greater<pair<int,int>>>   pq;
        for(auto it:mp){
            int num=it.first;
            int freq=it.second;
            if(pq.size()<k) 
                pq.push({freq,num});
            else if(pq.size()>=k && pq.top().first<freq ){
                pq.pop();
                pq.push({freq,num});
            }
        }

        vector<int> ans;
        while(!pq.empty()){
            pair<int,int> curr=pq.top();
            pq.pop();
            ans.push_back(curr.second);
        }

        return ans;
    }
};