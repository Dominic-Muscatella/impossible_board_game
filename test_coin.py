import numpy as np
def natural_p(board):
    l=[]
    for x in range(6):

        if x == 0: 
            l.append(sum(board[:,0]+
                        board[:,2]+
                        board[:,4]+
                        board[:,6])%2)
        if x == 1:
            l.append(sum(board[:,0]+
                        board[:,1]+
                        board[:,4]+
                        board[:,5])%2)
        if x == 2:
            l.append(sum(board[:,0]+
                        board[:,1]+
                        board[:,2]+
                        board[:,3])%2)
            
        if x == 3: 
            l.append(sum(board[0,:]+
                        board[2,:]+
                        board[4,:]+
                        board[6,:])%2)
        if x == 4:
            l.append(sum(board[0,:]+
                        board[1,:]+
                        board[4,:]+
                        board[5,:])%2)
        if x == 5:
            l.append(sum(board[0,:]+
                        board[1,:]+
                        board[2,:]+
                        board[3,:])%2)  
    l.reverse()                                 
    return l
def test_coin():
    nums = np.random.choice([0, 1], size=64, p=[.5, .5])            #generate a random board
    board = nums.reshape(8,8)                                       #reshape
    key = np.random.choice(range(64))                               #assign key to random location
    print(board)
    print("warden chooses key location : {}th square".format(key))
    l=natural_p(board)                                              #get the natural parity of the board as 6 bits
    natural_parity=int(''.join(str(c)for c in l[:6]),2)             #convert bits to a proper integer 
    bit_to_flip=key ^ natural_parity                                #xor the key bits with the parity bits to get the coin-to-flip
    print("1st prisoner will flip the {}th coin".format(bit_to_flip))
    flipped=nums
    flipped[bit_to_flip]= int(not flipped[bit_to_flip])             #create identical board with the flipped coin
    flipped_board=flipped.reshape(8,8)                              #reshape
                                                                    #exit prisoner 1, enter prisoner 2
    l=natural_p(flipped_board)                                      #get the parity of this board as 6 bits
    location_from_flip=int(''.join(str(int(not c))for c in l[:6]),2)#flip the bits and convert to an integer 
    print("so second prisoner chooses the {}th square".format(location_from_flip)) 
    assert key == location_from_flip                                #assert you've foiled the warden
