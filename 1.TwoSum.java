import java.util.*;

class Solution {
    public int[] twoSum(int[] nums, int target) {

        Map<Integer, Integer> output = new HashMap<Integer, Integer>();

        for (int i = 0; i < nums.length; i++) {
            Integer zwErgebnis = target - nums[i];
            if (zwErgebnis > 0) {
                output.put(nums[i], i);
            }
        };
        return output.values().stream().mapToInt(i -> i).toArray();
    }
    public static void main(String[] args) {
        Solution s = new Solution();
        System.out.println(Arrays.toString(s.twoSum(new int[] { 2, 7, 11, 15 }, 9)));
        System.out.println(Arrays.toString(s.twoSum(new int[] { 3,2,4 }, 6)));
        System.out.println(Arrays.toString(s.twoSum(new int[] { 3,3 }, 6)));
    }
}