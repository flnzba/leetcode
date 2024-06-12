class TwoSum_1 {
    int[] nums = { 2, 7, 11, 15 };
    int target = 9;
    int[] result;

    // int[] nums = { 3, 2, 4 };
    // int target = 6;

    // int[] nums = { 3, 3 };
    // int target = 6;

    public int[] twoSum(int[] nums, int target) {
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j < nums.length; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[] {i, j};
                }
            }
        }
        throw new IllegalArgumentException("No two sum solution");

    }

    public static void main(String[] args) {
        TwoSum_1 solution = new TwoSum_1();
        int[] result = solution.twoSum(solution.nums, solution.target);

        for (int i : result) {
            System.out.print(i + " ");
        }
    }
}