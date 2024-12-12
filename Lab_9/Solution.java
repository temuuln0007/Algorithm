/*
Холбосон жагсаалт (linked list)-ын толгойд (head) өгөгдсөн бол холбосон жагсаалтад цикл байгаа эсэхийг тодорхойлно уу.

Холбосон жагсаалт нь циклтэй гэж тооцогддог бол жагсаалтын зарим нэг узел (node)-оос дахин очих боломжтой байдаг, энэ нь дараагийн заавар (next pointer)-аар дамжуулан дахин очих боломжтой байдаг. Дотор нь pos гэж нэрлэгдсэн утга нь сүүлчийн узелийн дараах заавар (next pointer)-ыг холбосон узелийн индексийг зааж өгнө. Харин pos-ийг параметр болгон оруулахгүй.

Холбосон жагсаалт циклтэй бол үнэн (true), циклгүй бол худал (false) буцаана уу.
*/

public class Solution {
    public boolean hasCycle(ListNode head) {
        ListNode fast = head;
        ListNode slow = head;

        while (fast != null && fast.next != null) {
            fast = fast.next.next;
            slow = slow.next;

            if (fast == slow) {
                return true;
            }
        }

        return false;        
    }
}