class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int groupSize) {
        if(hand.size() % groupSize != 0) return false;

        priority_queue<int,vector<int>,greater<int>> pq;
        unordered_map<int,int> mp;
        for(int i=0;i<hand.size();i++){
            if(mp.find(hand[i])!=mp.end())
               mp[hand[i]]++;
            else{
                pq.push(hand[i]);
                mp[hand[i]]=1;
            }
        }
        
         while(!pq.empty()){
            if(mp[pq.top()]==0){
                pq.pop();
                continue;
            }
            int x=pq.top();
            for(int i=x; i< x+groupSize; i++){
                if(mp[i]==0)
                   return false;
                mp[i]--;
            }
         }
         return true;
    }
};