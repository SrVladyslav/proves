## 
## This program is free software; you can redistribute it and/or modify it
## under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 3 of the License, or
## (at your option) any later version.
## 
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.
## 
## You should have received a copy of the GNU General Public License
## along with this program.  If not, see <http://www.gnu.org/licenses/>.

## -*- texinfo -*- 
## @deftypefn {} {@var{retval} =} Wilson (@var{input1}, @var{input2})
##
## @seealso{}
## @end deftypefn

## Author: MAZURKEVYCH <vlama@EVIRL-015-OK>
## Created: 2020-03-19

function [X,X_label] = Wilson (X1,X_label)
  error = true; X = X1;
  iter = 1;
  errores = 0;
  printf("Wilson?\n========\n");
  activeRows = [1:rows(X)]';

  while(error == true)
    printf("\n\nRunning %d iter...  \n===============================\n", iter);iter ++;
    error = false;
    % Starting the for loop
    i = 1;
    while(i <= rows(activeRows)) 
      fallos = 0;    
      % Starting with our modified KNN
      %==========================================
      % First we look for distances relative to activeRows
      D = L2dist(X(activeRows,:), X(activeRows(i),:));
      % Now, as the better distance will be the self element, so we must take the 
      % second position from nearest ones
      [D, idx] = sort(D, 'ascend');
      % Deleting the self value
      idx = idx(2);
      % Given the nearest element class, we proove if they are same
      %==========================================
      if(X_label(activeRows(i),:) != X_label(activeRows(idx),:))
         % Now just drop him from active list
         printf("Borrando: %d,%d\n",X(activeRows(i,:),1),X(activeRows(i,:),2));
         activeRows(i,:) = [];
         error = true;
         i--;
      endif
      i ++;
    endwhile
   endwhile 
   X = X(activeRows,:);
   X_label = X_label(activeRows,:);
   printf("[ Done! ]\n");
endfunction