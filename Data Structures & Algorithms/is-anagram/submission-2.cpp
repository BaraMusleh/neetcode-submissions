class Solution {
public:
        bool isAnagram(string s, string t) {
            if (s.size() != t.size()){
                return false ;
            }

            unordered_map<char, int> seen;

            for (char c : s){
                seen[c]++;
            }

            for (char c : t){
                auto it = seen.find(c) ;
                if (it == seen.end() || it->second == 0){
                    return false ;
                }
                it->second -- ;
            }
            return true ;   
        }
};
