class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        parts = path.split('/')

        for part in parts:
            if part == '..':
                if stack:
                    stack.pop()  # Go up one directory (if possible)
            elif part and part != '.':  
                stack.append(part)  # Add valid directory/file names

        return '/' + '/'.join(stack)