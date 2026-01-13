class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        # split the path by slashs
        parts = path.split('/')
        
        for p in parts:
            # ignore current dir or emty strings
            if p == "." or p == "":
                continue
            # go back up one levl if possible
            elif p == "..":
                if stack:
                    stack.pop()
            else:
                # add valid directry
                stack.append(p)
                
        # join everythng back together
        return "/" + "/".join(stack)