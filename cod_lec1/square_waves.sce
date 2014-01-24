num_points = 5
t_list=linspace(-%pi,%pi,num_points)
res=ones(num_points)


for i=1:num_points
    s = 0;
    t = t_list(i);
    for k = 1:99
        s = s + 4*sin((2*k-1)*t)/((2*k-1)*%pi);
    end
    res(i) = s;
end
