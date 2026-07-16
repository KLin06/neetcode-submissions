class Solution {
    public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] ans = new int[length];

        ans[length - 1] = nums[length - 1];
        for(int i = nums.length - 2; i >= 0; i--){
            ans[i] = ans[i + 1] * nums[i];
        }

        for(int i = 1; i < length; i++){
            nums[i] *= nums[i - 1];
        }

        for(int i = 0; i < length; i++){
            int pre = 1;
            int post = 1;

            if (i - 1 >= 0)
                pre = nums[i - 1];
            if (i + 1 < length)
                post = ans[i + 1];
            
            ans[i] = pre * post;
        }

        return ans;
    }
}  
