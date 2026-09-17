from typing import List

class Solution:

    def encoder(self, s):
        # Store encoded ASCII values for one string.
        res = ""

        # Convert each character into its ASCII value.
        for ch in s:

            # Add ASCII value followed by comma.
            res += str(ord(ch)) + ","

        # Return encoded string.
        return res

    def decoder(self, s):
        # Store decoded result.
        res = ""

        # Store current ASCII number as string.
        temp = ""

        # Loop through encoded string.
        for ch in s:

            # If comma is found, current ASCII number is complete.
            if ch == ",":

                # Convert ASCII number back to character.
                res += chr(int(temp))

                # Reset temp for next character.
                temp = ""

            # Otherwise, keep building ASCII number.
            else:

                # Add digit to temp.
                temp += ch

        # Return decoded string.
        return res

    def encode(self, strs: List[str]) -> str:
        # Store final encoded string.
        ans = ""

        # Encode each string separately.
        for s in strs:

            # Add encoded string and separate strings using underscore.
            ans += self.encoder(s) + "_"

        # Return final encoded result.
        return ans

    def decode(self, s: str) -> List[str]:
        # If encoded string is empty, return empty list.
        if not s:

            # Return empty list.
            return []

        # Store final decoded strings.
        strs = []

        # Remove last underscore and split encoded strings by underscore.
        parts = s[:-1].split("_")

        # Decode each encoded string.
        for part in parts:

            # Decode one string and add it to result.
            strs.append(self.decoder(part))

        # Return decoded list.
        return strs