public class Solution {
    public bool IsPalindrome(string s) {
        s= s.ToLower().Replace(" ","");
        int left = 0 , right=s.Length-1;

        while(left < right){
            while(left <right && !char.IsLetterOrDigit(s[left])) left++;
            while(left <right && !char.IsLetterOrDigit(s[right])) right--;
            if(s[left]!=s[right]) return false;
            left++;
            right--;
        }
        return true ;
    }
}