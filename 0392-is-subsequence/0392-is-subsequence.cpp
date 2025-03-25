class Solution {
public:
    bool isSubsequence(string s, string t) {
        int s_pointer = 0;
        int t_pointer = 0;

        while(s_pointer < s.length() && t_pointer < t.length()){
            if(s[s_pointer] == t[t_pointer]){
                s_pointer++;
            }
            t_pointer++;
        }
        if(s_pointer == s.length()){
            return true;
        }
        return false;
    }
};