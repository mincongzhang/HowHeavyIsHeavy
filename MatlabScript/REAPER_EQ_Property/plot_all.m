function plot_all()
hold on;
plot_bass();
plot_mid();
plot_treble();
xlabel('frequency');ylabel('average spectrogram');
%title('treble weight');
axis([0 100 0 15]);
end

