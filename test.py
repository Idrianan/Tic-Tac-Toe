from main import check_symbol,check_if_draw, check_win


def test_check_symbol():
    neutral_field = [['X','Y','X'],['Y',None,'Y'],['X','Y','X']]
    draw_field = [["Y",'Y','X'],['X','X','Y'],['Y','X','X']]
    x_won = [['X','X','X'],['Y',None,'Y'],['X','Y','X']]
    assert check_symbol(draw_field,(0,0)) == 1
    assert check_symbol(neutral_field,(1,1)) == 0
    assert check_symbol(neutral_field,(2,1)) == 3
    assert check_symbol(x_won,(2,1)) == 2

def test_check_if_draw():
    neutral_field = [['X','Y','X'],['Y',None,'Y'],['X','Y','X']]
    draw_field = [["Y",'Y','X'],['X','X','Y'],['Y','X','X']]
    x_won = [['X','X','X'],['Y',None,'Y'],['X','Y','X']]
    assert check_if_draw(neutral_field)== 0
    assert check_if_draw(draw_field)== 1
    assert check_if_draw(x_won)== 0

def test_check_win():
    neutral_field = [['X','Y','X'],['Y',None,'Y'],['X','Y','X']]
    draw_field = [["Y",'Y','X'],['X','X','Y'],['Y','X','X']]
    x_won = [['X','X','X'],['Y',None,'Y'],['X','Y','X']]
    y_won = [["Y",'Y','Y'],['X','X','Y'],['Y','X','X']]
    assert check_win(neutral_field,"Y") == 0
    assert check_win(draw_field,"Y") == 0
    assert check_win(x_won,"X") == 1
    assert check_win(x_won,"Y") == 0
    assert check_win(y_won,"Y") == 1
    assert check_win(y_won,"X") == 0

test_check_if_draw()
test_check_symbol()
test_check_win()