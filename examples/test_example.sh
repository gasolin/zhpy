echo "test zhpy as script:"
zhpy -c "印出 '哈囉'"
zhpy -c "打印 '哈啰'"

echo "test zhpy examples:"

echo "zhpy hello example:"

cd hello
zhpy hello.twpy n_hello.py
zhpy -p hello.twpy
cd ..

echo "zhpy in/out example:"
cd inout
zhpy -i inout.twpy -o n_inout.py
zhpy -p inout.twpy
cd ..

echo "zhpy loop example:"
cd loop
zhpy -p tabl.twpy
cd ..

echo "zhpy game example:"
echo "pygame module required. Use 'Ctrl+c' to escape"

cd game
zhpy -p game.twpy
cd ..

echo "finish"