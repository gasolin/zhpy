echo "zhpy hello example"

cd hello
zhpy hello.py n_hello.py
zhpy -p hello.py
cd ..

echo "zhpy in/out example"
cd inout
zhpy -i inout.py -o n_inout.py
zhpy -p inout.py
cd ..

echo "zhpy loop example"
cd loop
zhpy -p tabl.py
cd ..

echo "zhpy game example, pygame module required. Use 'Ctrl+c' to escape"

cd game
zhpy -p game.py
cd ..

echo "test zhpy as script:"
zhpy -c "印出 '哈囉'"
zhpy -c "打印 '哈啰'"

echo "finish"