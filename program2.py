def decode_message( s: str, p: str) -> bool:

# write your code here
# return True if the message is decoded successfully, False otherwise
        if s==p:
                return True
        else:
                for i in range(len(s)):
                        for j in range(len(p)):
                                if s[i]!= p[j] and p[j]!="*" and p[j]!= "?":
                                        return False
                                elif p[j]=="*" and j==len(p):
                                        return True
                                elif p[j]=="?":
                                        p=p[:j]+s[i]+p[j+1:]
                                        if s==p:
                                                return True
                                

  
        return False