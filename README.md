# PythonGame
SchoolProject
=========
2021/08/09 update
<ul>
<li>검은 배경화면 만들기</li>
</ul>


2021/08/11 update

추가한 것
<ul>
<li>게임화면에 비행기 표시를 완료 하였습니다.
<li>적 비행기가 주기적으로 떨어지게끔 설정하고 표시했습니다.
<li>LEFT-CTRL누를시 총알 나가게 표시했습니다.
<li>적 비행기와 충돌 시, gameover
<li>총알과 적 비행기가 만날 때, score + 1
</ul>

수정한 것.
<ul>
<li>비행기 사이즈가 너무 크게 표시되어 fighter = pygame.transform.scale(fighter,(fighter_width,fighter_height)) 로 해결 하였습니다.
<li>기존 비행기는 좌우로만 움직일 수 있어서 상하좌우, 대각선으로 움직일 수 있게 수정했습니다.
<li>한쪽 방향으로만 갈 경우, 급속도로 빨라지는 현상을 수정했습니다..(가속도에 제한 둠)
<li>적 비행기 회전하여 방향설정, 적비행기 크기 조정.
<li>총알이 비행기 정 중앙에서 나오도록 값 조정.
<li>비행기가 적 비행기 뒤로가도 gameover되는 현상 수정.
</ul>

다음에 할 것.
<ul>
<li>총알과 적비행기 충돌시 파괴모션 추가
</ul>