class KthLargest {
public:
    priority_queue<int,vector<int>,greater<int>> pq;
    int p;
    KthLargest(int k, vector<int>& nums) {
        int n=nums.size();
        p=k;
        for(int i=0;i<n;i++){
            if(i<k)
                pq.push(nums[i]);
            else{
                if(pq.top()<nums[i]){
                    pq.pop();
                    pq.push(nums[i]);
                }
            }
        }
    }
    
    int add(int val) {
        if(pq.size()<p){
            pq.push(val);
            return pq.top();
        }else if(pq.top()<val){
            pq.pop();
            pq.push(val);
        }
        return pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */