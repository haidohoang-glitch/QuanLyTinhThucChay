# Stored Procedure: `BPTC_NhapChiTieu_Insert_ChiTieu`

- **Loại**: SQL_STORED_PROCEDURE
- **Ngày tạo**: 2015-06-11 18:17:51.270000
- **Ngày sửa cuối**: 2015-06-11 18:17:51.270000

## Parameters

| Parameter | Type | Output |
|-----------|------|--------|
| `@Nam` | `int(4)` | No |
| `@LoaiTienID` | `int(4)` | No |
| `@LevelChiTieu` | `int(4)` | No |
| `@NguoiLog` | `nvarchar(510)` | No |
| `@LoaiLog` | `int(4)` | No |
| `@Values` | `BPTC_NhapChiTieu_ThongTinChiTieu_Type` | No |

## Definition (Source Code)

```sql

CREATE PROC [dbo].[BPTC_NhapChiTieu_Insert_ChiTieu]
    (
      @Nam INT ,
      @LoaiTienID INT ,      
      @LevelChiTieu INT ,
      @NguoiLog NVARCHAR(255) ,
      @LoaiLog INT ,
      @Values BPTC_NhapChiTieu_ThongTinChiTieu_Type READONLY
    )
AS 
    BEGIN
        SELECT  *
        INTO    #T
        FROM    @Values
        WHERE   ChiTieuID <= 0
		 
        DECLARE @ChiTieuBoPhan NVARCHAR(50)
        DECLARE @TenLoaiTien NVARCHAR(100)
                        
        SELECT  @TenLoaiTien = CASE @LoaiTienID
                                 WHEN 1 THEN N'Thực chạy'
                                 WHEN 2 THEN N'Đánh số'
                                 WHEN 3 THEN N'Bản cứng'
                                 ELSE N'Hóa đơn'
                               END        
        	
        INSERT  INTO dbo.ThongTinChiTieu
                ( ChiTieuBoPhan ,
                  DmChiTieuBoPhanREF ,
                  LevelChiTieu ,
                  ThoiGianBatDau ,
                  ThoiGianKetThuc ,
                  DoanhSoChiTieu ,
                  LoaiTien ,
                  TenLoaiTien ,
                  NguoiDangKy ,
                  NguoiXacNhan ,
                  GhiChu ,
                  CreatedBy ,
                  CreatedAt ,
                  LastModifiedBy ,
                  LastModifiedAt ,
                  DeleteStatus ,
                  PrintStatus ,
                  RecordStatus
                )
                SELECT  (SELECT  TenSanPham
							FROM    dbo.DmNhomSanPhamBaoCao
							WHERE   DmSanPhamREF = T1.SanPhamID
						) , -- ChiTieuBoPhan - nvarchar(50)
                        T1.SanPhamID , -- DmChiTieuBoPhanREF - int
                        @LevelChiTieu , -- LevelChiTieu - int                  
                        DATEADD(mm, ( @Nam - 1900 ) * 12 + T1.Thang - 1, 0) , -- ThoiGianBatDau - datetime
                        DATEADD(s, -1,
                                DATEADD(mm,
                                        DATEDIFF(m, 0,
                                                 DATEADD(mm,
                                                         ( @Nam - 1900 ) * 12
                                                         + T1.Thang - 1, 0))
                                        + 1, 0)) , -- ThoiGianKetThuc - datetime
                        T1.DoanhSoChiTieu , -- DoanhSoChiTieu - numeric
                        @LoaiTienID , -- LoaiTien - int
                        @TenLoaiTien , -- TenLoaiTien - nvarchar(100)
                        NULL , -- NguoiDangKy - nvarchar(100)
                        NULL , -- NguoiXacNhan - nvarchar(100)
                        N'NEW_RECORD' , -- GhiChu - nvarchar(max)
                        @NguoiLog , -- CreatedBy - nvarchar(100)
                        GETDATE() , -- CreatedAt - datetime
                        @NguoiLog , -- LastModifiedBy - nvarchar(100)
                        GETDATE() , -- LastModifiedAt - datetime
                        0 , -- DeleteStatus - int
                        0 , -- PrintStatus - int
                        0  -- RecordStatus - int
                FROM    #T T1                
                        
        INSERT  INTO dbo.ThongTinChiTieuLog
                ( ChiTieuBoPhan ,
                  DmChiTieuBoPhanREF ,
                  LevelChiTieu ,
                  ThoiGianBatDau ,
                  ThoiGianKetThuc ,
                  DoanhSoChiTieu ,
                  LoaiTien ,
                  TenLoaiTien ,
                  NguoiDangKy ,
                  NguoiXacNhan ,
                  GhiChu ,
                  ThongTinChiTieuREF ,
                  LoaiLog ,
                  NguoiLog ,
                  NgayLog ,
                  CreatedBy ,
                  CreatedAt ,
                  LastModifiedBy ,
                  LastModifiedAt ,
                  DeleteStatus ,
                  PrintStatus ,
                  RecordStatus		        
                )
                SELECT  ChiTieuBoPhan ,
                        DmChiTieuBoPhanREF ,
                        LevelChiTieu ,
                        ThoiGianBatDau ,
                        ThoiGianKetThuc ,
                        DoanhSoChiTieu ,
                        LoaiTien ,
                        TenLoaiTien ,
                        NguoiDangKy ,
                        NguoiXacNhan ,
                        GhiChu ,
                        ThongTinChiTieuID ,
                        @LoaiLog ,
                        @NguoiLog ,
                        GETDATE() ,
                        @NguoiLog ,
                        GETDATE() ,
                        @NguoiLog ,
                        GETDATE() ,
                        0 ,
                        0 ,
                        0
                FROM    dbo.ThongTinChiTieu
                WHERE   GhiChu = N'NEW_RECORD'		          	             
				
        UPDATE  dbo.ThongTinChiTieu
        SET     GhiChu = NULL
        WHERE   GhiChu = N'NEW_RECORD'		
		
        DROP TABLE #T
        
    END

```
