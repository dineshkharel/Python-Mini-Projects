def print_board(combo):
    print(f"""
 {combo[0][0] or ' '} | {combo[0][1] or ' '} | {combo[0][2] or ' '}
---+---+---
 {combo[1][0] or ' '} | {combo[1][1] or ' '} | {combo[1][2] or ' '}
---+---+---
 {combo[2][0] or ' '} | {combo[2][1] or ' '} | {combo[2][2] or ' '}
""")
