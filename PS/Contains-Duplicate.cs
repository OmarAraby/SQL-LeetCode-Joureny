public class Solution {
    public bool ContainsDuplicate(int[] nums) {
         var seen= new HashSet<int>();
        foreach(var x in nums){
            if(!seen.Add(x)) return true ;
        }
        return false;
        
    }
}