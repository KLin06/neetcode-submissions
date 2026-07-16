class Solution {
    public void createSubset(int index, int[] nums, List<Integer> stack, List<List<Integer>> sol){
        if(index == nums.length){
            sol.add(new ArrayList<>(stack));
        } else if (index < nums.length){
            stack.add(nums[index]);
            createSubset(index + 1, nums, stack, sol);
            stack.remove(stack.size() - 1);
            createSubset(index + 1, nums, stack, sol);
        }
    }

    public List<List<Integer>> subsets(int[] nums) {
        List<List<Integer>> sol = new ArrayList<>();
        List<Integer> stack = new ArrayList<>();

        createSubset(0, nums, stack, sol);
        return sol;
    }
}
