# Stored Procedure: `sp_CheckPhanBoDaTreoThayDoi`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2020-09-16 11:52:34.347000
- **Ngày sửa cuối**: 2020-09-16 14:14:32.240000

## Parameters

*(Không có tham số)*

## Definition (Source Code)

```sql

CREATE proc sp_CheckPhanBoDaTreoThayDoi
as
begin
select A.contract_number [SoHopDong], A.contract_detail_id ID_PhanBo,
A.HTQC HTQC_Treo,B.HTQC,
A.SanPham SanPham_Treo,  B.SanPham,
A.Discount CK_Treo, B.PERCENT_DISCOUNT_TOTAL CK,
A.quantity SL_Treo, dbo.FormatNumber(A.unitprice) DonGia_Treo,  --B.DELETED_STATUS TrangThaiXoaPB,
(case when A.HTQC <> B.HTQC then 'x' else '' end) LechHTQC,
(case when A.SanPham <> B.SanPham then 'x' else '' end) LechSanPham,
(case when A.Discount <> B.PERCENT_DISCOUNT_TOTAL then 'x' else '' end) LechCK,
(case when B.LoaiBanner ='MuaNgoai' then 'x' else '' end) ChuyenMN
from (
select contract_number, contract_id,contract_detail_id,product_formality_id, f.NAME HTQC, product_id,p.NAME SanPham, --brand_id, 
Discount, quantity, unitprice from [asd14].thuctreo.dbo.thuctreo_chiphi cp
left join [asd14].contract.dbo.contracts c on cp.contract_id = c.id
left join [asd14].contract.dbo.PRODUCT_FORMALITY f on f.id = cp.product_formality_id
left join [asd14].contract.dbo.PRODUCTS p on p.id = cp.product_id
where cp.deletedstatus = 0 and not ( cp.quantity = 0 or cp.unitprice = 0)
and contract_detail_id not in (505842,544957,580596,84066)
)A
left join
(
select contract_id,ct.id ,product_formality_id,f.NAME HTQC, product_id,p.NAME SanPham, --b.brand_id, 
PERCENT_DISCOUNT_TOTAL, ct.DELETED_STATUS,(case when b.value = 18 then 'MuaNgoai' else''end)LoaiBanner
from [asd14].contract.dbo.contract_details ct 
left join [asd14].contract.dbo.CONTRACT_DETAIL_PRODUCT_PROPERTIES b on ct.id = b.contract_detail_id and b.PRODUCT_CONFIG_PROPERTY_ID =5  and b.DELETED_STATUS =0
left join [asd14].contract.dbo.PRODUCT_FORMALITY f on f.id = ct.product_formality_id
left join [asd14].contract.dbo.PRODUCTS p on p.id = ct.product_id
where ct.id not in (505842,544957,580596,84066)
--and ct.id =588827
)B
on A.contract_detail_id = B.id
where 1=1 and --isnull(A.brand_id,'') <> isnull(B.brand_id,'')
 ( isnull(A.product_formality_id,0) <> isnull(B.product_formality_id,0)
or isnull(A.product_id,0) <> isnull(B.product_id,0)
or isnull(A.Discount,0) <> isnull(B.PERCENT_DISCOUNT_TOTAL,0)
)

order by A.contract_id desc, A.contract_detail_id
end
```
