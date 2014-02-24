function plot_treble()
for j=1:10
    %B=['b',num2str(j)];
    %M=['m',num2str(j)];
    T=['t',num2str(j)];
    audio=wavread(['b5m5',T,'.wav']);
    audio1=audio(:,1);
    audio2=audio(:,2);
    audio12=audio1+audio2;
    audio12m = max(max(audio12),abs(min(audio12))); % find the max value
    audio_fin=audio12./audio12m; % normalize
    [S,F,T,P] = spectrogram(audio_fin,256);

    M=size(S);
    row=M(1);%列数 number of column
    S(:,1);%第一列 size(X)的结果显示(行,列)
        for i=1:row
            value(i)=mean (abs(S(i,:)));
        end
    set(gca,'xscale','log');
    plot(value,'-.');
    hold on;

end
end

